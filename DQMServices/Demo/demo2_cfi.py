import FWCore.ParameterSet.Config as cms

demo2 = cms.EDProducer('DemoGlobalDQMEDAnalyzer',
  folder = cms.string('MY_FOLDER'),
  mightGet = cms.optional.untracked.vstring
)
