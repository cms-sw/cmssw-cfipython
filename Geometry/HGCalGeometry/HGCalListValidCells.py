import FWCore.ParameterSet.Config as cms

def HGCalListValidCells(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalListValidCells',
    detector = cms.string('HGCalEESensitive'),
    partialType = cms.int32(16),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
