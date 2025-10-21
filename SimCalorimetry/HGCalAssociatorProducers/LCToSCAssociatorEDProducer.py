import FWCore.ParameterSet.Config as cms

def LCToSCAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('LCToSCAssociatorEDProducer',
    label_scl = cms.InputTag('mix', 'MergedCaloTruth'),
    label_lcl = cms.InputTag('hgcalMergeLayerClusters'),
    associator = cms.InputTag('scAssocByEnergyScoreProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
