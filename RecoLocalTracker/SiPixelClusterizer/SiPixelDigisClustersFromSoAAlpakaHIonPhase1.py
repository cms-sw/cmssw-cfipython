import FWCore.ParameterSet.Config as cms

def SiPixelDigisClustersFromSoAAlpakaHIonPhase1(**kwargs):
  mod = cms.EDProducer('SiPixelDigisClustersFromSoAAlpakaHIonPhase1',
    src = cms.InputTag('siPixelDigisSoA'),
    clusterThreshold_layer1 = cms.int32(2000),
    clusterThreshold_otherLayers = cms.int32(4000),
    produceDigis = cms.bool(True),
    storeDigis = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
