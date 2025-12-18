import FWCore.ParameterSet.Config as cms

def PATElectronPuppiIsolationUpdater(*args, **kwargs):
  mod = cms.EDProducer('PATElectronPuppiIsolationUpdater',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
