import FWCore.ParameterSet.Config as cms

def PATPhotonPuppiIsolationUpdater(*args, **kwargs):
  mod = cms.EDProducer('PATPhotonPuppiIsolationUpdater',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
