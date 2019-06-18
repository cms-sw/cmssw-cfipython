import FWCore.ParameterSet.Config as cms

test = cms.EDAnalyzer('TestDescriptionComments',
  sswitch = cms.string('b'),
  y1 = cms.required.double,
  y2 = cms.required.double,
  mightGet = cms.optional.untracked.vstring
)
