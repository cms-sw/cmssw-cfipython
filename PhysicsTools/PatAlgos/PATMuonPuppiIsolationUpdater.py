import FWCore.ParameterSet.Config as cms

def PATMuonPuppiIsolationUpdater(*args, **kwargs):
  mod = cms.EDProducer('PATMuonPuppiIsolationUpdater',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
