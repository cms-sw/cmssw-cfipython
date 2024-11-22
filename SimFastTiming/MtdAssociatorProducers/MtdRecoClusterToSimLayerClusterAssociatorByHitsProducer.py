import FWCore.ParameterSet.Config as cms

def MtdRecoClusterToSimLayerClusterAssociatorByHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('MtdRecoClusterToSimLayerClusterAssociatorByHitsProducer',
    energyCut = cms.double(5),
    timeCut = cms.double(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
