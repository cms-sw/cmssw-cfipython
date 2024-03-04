import FWCore.ParameterSet.Config as cms

def SiPixelStatusProducer(**kwargs):
  mod = cms.EDProducer('SiPixelStatusProducer',
    SiPixelStatusProducerParameters = cms.PSet(
      pixelClusterLabel = cms.untracked.InputTag('siPixelClusters', '', 'RECO'),
      badPixelFEDChannelCollections = cms.VInputTag('siPixelDigis')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
