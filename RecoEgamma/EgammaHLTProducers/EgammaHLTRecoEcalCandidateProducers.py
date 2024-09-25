import FWCore.ParameterSet.Config as cms

def EgammaHLTRecoEcalCandidateProducers(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTRecoEcalCandidateProducers',
    scHybridBarrelProducer = cms.InputTag('correctedHybridSuperClusters'),
    scIslandEndcapProducer = cms.InputTag('correctedEndcapSuperClustersWithPreshower'),
    recoEcalCandidateCollection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
