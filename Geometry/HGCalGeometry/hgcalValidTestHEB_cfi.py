import FWCore.ParameterSet.Config as cms

hgcalValidTestHEB = cms.EDAnalyzer('HGCalValidTest',
  detector = cms.string('HGCalHEScintillatorSensitive'),
  mightGet = cms.optional.untracked.vstring
)
