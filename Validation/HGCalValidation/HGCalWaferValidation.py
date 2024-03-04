import FWCore.ParameterSet.Config as cms

def HGCalWaferValidation(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferValidation',
    GeometryFileName = cms.FileInPath('Validation/HGCalValidation/data/geomnew_corrected_360.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
