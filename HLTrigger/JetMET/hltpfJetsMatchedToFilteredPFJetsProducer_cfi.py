import FWCore.ParameterSet.Config as cms

hltpfJetsMatchedToFilteredPFJetsProducer = cms.EDProducer('HLTPFJetsMatchedToFilteredPFJetsProducer',
  src = cms.InputTag('hltPFJets'),
  triggerJetsFilter = cms.InputTag('hltSingleJet240Regional'),
  triggerJetsType = cms.int32(85),
  maxDeltaR = cms.double(0.5),
  mightGet = cms.optional.untracked.vstring
)
