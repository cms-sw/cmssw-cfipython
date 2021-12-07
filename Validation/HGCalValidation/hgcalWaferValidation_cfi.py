import FWCore.ParameterSet.Config as cms

hgcalWaferValidation = cms.EDAnalyzer('HGCalWaferValidation',
  GeometryFileName = cms.FileInPath('Validation/HGCalValidation/data/geomnew_corrected_360.txt'),
  mightGet = cms.optional.untracked.vstring
)
