import FWCore.ParameterSet.Config as cms

MPIService = cms.Service('MPIService',
  pmix_server_uri = cms.optional.untracked.string
)
