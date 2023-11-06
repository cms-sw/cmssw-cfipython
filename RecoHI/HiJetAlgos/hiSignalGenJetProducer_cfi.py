import FWCore.ParameterSet.Config as cms

hiSignalGenJetProducer = cms.EDProducer('HiSignalGenJetProducer',
  src = cms.InputTag('akHiGenJets'),
  mightGet = cms.optional.untracked.vstring
)
