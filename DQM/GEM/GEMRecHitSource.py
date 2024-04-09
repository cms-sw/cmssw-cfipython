import FWCore.ParameterSet.Config as cms

def GEMRecHitSource(**kwargs):
  mod = cms.EDProducer('GEMRecHitSource',
    recHitsInputLabel = cms.InputTag('gemRecHits'),
    runType = cms.untracked.string('online'),
    idxFirstDigi = cms.int32(0),
    numDivideEtaPartitionInRPhi = cms.int32(10),
    clsMax = cms.int32(10),
    ClusterSizeBinNum = cms.int32(9),
    logCategory = cms.untracked.string('GEMRecHitSource'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod