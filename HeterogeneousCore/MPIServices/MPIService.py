import FWCore.ParameterSet.Config as cms

def MPIService(**kwargs):
  mod = cms.Service('MPIService',
    pmix_server_uri = cms.optional.untracked.string
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
