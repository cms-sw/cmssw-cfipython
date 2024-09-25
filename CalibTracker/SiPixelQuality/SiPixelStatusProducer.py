import FWCore.ParameterSet.Config as cms

def SiPixelStatusProducer(*args, **kwargs):
  mod = cms.EDProducer('SiPixelStatusProducer',
    SiPixelStatusProducerParameters = cms.PSet(
      pixelClusterLabel = cms.untracked.InputTag('siPixelClusters', '', 'RECO'),
      badPixelFEDChannelCollections = cms.VInputTag('siPixelDigis')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
