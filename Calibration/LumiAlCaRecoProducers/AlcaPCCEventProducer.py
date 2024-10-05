import FWCore.ParameterSet.Config as cms

def AlcaPCCEventProducer(**kwargs):
  mod = cms.EDProducer('AlcaPCCEventProducer',
    pixelClusterLabel = cms.InputTag('siPixelClustersForLumi'),
    trigstring = cms.untracked.string('alcaPCCEvent'),
    savePerROCInfo = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
