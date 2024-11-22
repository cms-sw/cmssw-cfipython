import FWCore.ParameterSet.Config as cms

def MPIService(*args, **kwargs):
  mod = cms.Service('MPIService',
    pmix_server_uri = cms.optional.untracked.string
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
