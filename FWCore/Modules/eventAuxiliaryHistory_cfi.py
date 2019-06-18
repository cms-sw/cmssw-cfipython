import FWCore.ParameterSet.Config as cms

eventAuxiliaryHistory = cms.EDProducer('EventAuxiliaryHistoryProducer',
  historyDepth = cms.required.uint32,
  mightGet = cms.optional.untracked.vstring
)
