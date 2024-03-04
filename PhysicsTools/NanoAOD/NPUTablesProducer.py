import FWCore.ParameterSet.Config as cms

def NPUTablesProducer(**kwargs):
  mod = cms.EDProducer('NPUTablesProducer',
    src = cms.InputTag('slimmedAddPileupInfo'),
    pvsrc = cms.InputTag('offlineSlimmedPrimaryVertices'),
    zbins = cms.vdouble(),
    savePtHatMax = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
