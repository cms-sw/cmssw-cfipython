import FWCore.ParameterSet.Config as cms

hcalTestAnalyzer = cms.EDAnalyzer('HcalTestAnalyzer',
  mightGet = cms.optional.untracked.vstring
)
