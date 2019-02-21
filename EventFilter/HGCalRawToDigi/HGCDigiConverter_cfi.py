import FWCore.ParameterSet.Config as cms

HGCDigiConverter = cms.EDProducer('HGCDigiConverter',
  eeDigis = cms.InputTag('mix', 'HGCDigisEE'),
  fhDigis = cms.InputTag('mix', 'HGCDigisHEfront'),
  bhDigis = cms.InputTag('mix', 'HGCDigisHEback')
)
