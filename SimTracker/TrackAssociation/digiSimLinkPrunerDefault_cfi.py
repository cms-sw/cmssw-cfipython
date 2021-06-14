import FWCore.ParameterSet.Config as cms

digiSimLinkPrunerDefault = cms.EDProducer('DigiSimLinkPruner',
  pixelSimLinkSrc = cms.InputTag('simSiPixelDigis')
)
