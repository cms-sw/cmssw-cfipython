import FWCore.ParameterSet.Config as cms

def MTDMergedClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('MTDMergedClusterProducer',
    btlBarrel = cms.InputTag('mtdClusters', 'FTLBarrel'),
    etlEndcap = cms.InputTag('mtdClusters', 'FTLEndcap'),
    btlMergedClusterInstance = cms.string('FTLBarrel'),
    etlMergedClusterInstance = cms.string('FTLEndcap'),
    btlConstituentsInstance = cms.string('FTLBarrelConstituents'),
    etlConstituentsInstance = cms.string('FTLEndcapConstituents'),
    timeThreshold = cms.double(10),
    energyThreshold = cms.double(0),
    saveMergedClusterConstituents = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
