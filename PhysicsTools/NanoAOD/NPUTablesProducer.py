import FWCore.ParameterSet.Config as cms

def NPUTablesProducer(*args, **kwargs):
  mod = cms.EDProducer('NPUTablesProducer',
    src = cms.InputTag('slimmedAddPileupInfo'),
    pvsrc = cms.InputTag('offlineSlimmedPrimaryVertices'),
    zbins = cms.vdouble(),
    savePtHatMax = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod