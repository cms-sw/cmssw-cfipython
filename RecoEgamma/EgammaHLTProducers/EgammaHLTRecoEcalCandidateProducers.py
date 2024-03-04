import FWCore.ParameterSet.Config as cms

def EgammaHLTRecoEcalCandidateProducers(**kwargs):
  mod = cms.EDProducer('EgammaHLTRecoEcalCandidateProducers',
    scHybridBarrelProducer = cms.InputTag('correctedHybridSuperClusters'),
    scIslandEndcapProducer = cms.InputTag('correctedEndcapSuperClustersWithPreshower'),
    recoEcalCandidateCollection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
