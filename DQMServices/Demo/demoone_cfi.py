import FWCore.ParameterSet.Config as cms

demoone = cms.EDProducer('DemoOneDQMEDAnalyzer',
  folder = cms.string('MY_FOLDER'),
  mightGet = cms.optional.untracked.vstring
)
