import FWCore.ParameterSet.Config as cms

def SiPixelDigisClustersFromSoAPhase1(*args, **kwargs):
  mod = cms.EDProducer('SiPixelDigisClustersFromSoAPhase1',
    src = cms.InputTag('siPixelDigisSoA'),
    clusterThreshold_layer1 = cms.int32(2000),
    clusterThreshold_otherLayers = cms.int32(4000),
    produceDigis = cms.bool(True),
    storeDigis = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
