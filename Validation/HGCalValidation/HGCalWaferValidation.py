import FWCore.ParameterSet.Config as cms

def HGCalWaferValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferValidation',
    GeometryFileName = cms.FileInPath('Validation/HGCalValidation/data/geomnew_corrected_360.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
