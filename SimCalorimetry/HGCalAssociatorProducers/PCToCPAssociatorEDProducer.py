import FWCore.ParameterSet.Config as cms

def PCToCPAssociatorEDProducer(*args, **kwargs):
  mod = cms.EDProducer('PCToCPAssociatorEDProducer',
    label_cp = cms.InputTag('cpAssocByEnergyScoreProducer'),
    label_lc = cms.InputTag('mix', 'MergedCaloTruth'),
    associator = cms.InputTag('hgcalMergeLayerClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
