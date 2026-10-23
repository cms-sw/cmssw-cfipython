import FWCore.ParameterSet.Config as cms

def GEMPadDigiClusterSource(*args, **kwargs):
  mod = cms.EDProducer('GEMPadDigiClusterSource',
    padDigiClusterInputLabel = cms.InputTag('muonCSCDigis', 'MuonGEMPadDigiCluster'),
    runType = cms.untracked.string('online'),
    logCategory = cms.untracked.string('GEMPadDigiClusterSource'),
    bxMin = cms.int32(-15),
    bxMax = cms.int32(15),
    clsMax = cms.int32(9),
    ClusterSizeBinNum = cms.int32(9),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
