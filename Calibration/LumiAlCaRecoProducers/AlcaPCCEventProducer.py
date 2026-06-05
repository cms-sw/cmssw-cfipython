import FWCore.ParameterSet.Config as cms

def AlcaPCCEventProducer(*args, **kwargs):
  mod = cms.EDProducer('AlcaPCCEventProducer',
    pixelClusterLabel = cms.InputTag('siPixelClustersForLumi'),
    trigstring = cms.untracked.string('alcaPCCEvent'),
    savePerROCInfo = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
