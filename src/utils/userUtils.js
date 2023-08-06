const UserRoleEnum = Object.freeze({
    ADMIN: "Role_admin",
    REGI: "Role_regi",
    OPERATOR: "Role_operator",
    CLIENT: "Role_client"
  });

const UserStatusEnum = Object.freeze({
    ACTIVE: "A",
    INACTIVE: "I"
})

export { UserRoleEnum, UserStatusEnum };