import FWCore.ParameterSet.Config as cms

hltSiPixelClusterMultiplicityValueProducer = cms.EDProducer('HLTSiPixelClusterMultiplicityValueProducer',
  src = cms.InputTag(''),
  defaultValue = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
