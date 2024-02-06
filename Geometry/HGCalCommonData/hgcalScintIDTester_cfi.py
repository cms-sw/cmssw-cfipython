import FWCore.ParameterSet.Config as cms

hgcalScintIDTester = cms.EDAnalyzer('HGCalScintIDTester',
  nameSense = cms.string('HGCalHEScintillatorSensitive'),
  fileName = cms.string('errorScintD88.txt'),
  mightGet = cms.optional.untracked.vstring
)
