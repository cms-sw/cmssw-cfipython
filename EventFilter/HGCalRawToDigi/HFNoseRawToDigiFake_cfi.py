import FWCore.ParameterSet.Config as cms

HFNoseRawToDigiFake = cms.EDProducer('HFNoseRawToDigiFake',
  hfnoseDigis = cms.InputTag('simHFNoseUnsuppressedDigis', 'HFNose'),
  mightGet = cms.optional.untracked.vstring
)
