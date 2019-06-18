import FWCore.ParameterSet.Config as cms

triggerRatesMonitorClient = cms.EDProducer('TriggerRatesMonitorClient',
  dqmPath = cms.untracked.string('HLT/Datasets'),
  mightGet = cms.optional.untracked.vstring
)
