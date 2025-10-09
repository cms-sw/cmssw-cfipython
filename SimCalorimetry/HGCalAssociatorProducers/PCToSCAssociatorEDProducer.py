import FWCore.ParameterSet.Config as cms

def PCToSCAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('PCToSCAssociatorEDProducer',
    label_scl = cms.InputTag('scAssocByEnergyScoreProducer'),
    label_lcl = cms.InputTag('mix', 'MergedCaloTruth'),
    associator = cms.InputTag('hgcalMergeLayerClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
