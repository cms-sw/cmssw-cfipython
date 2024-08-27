import FWCore.ParameterSet.Config as cms

def BeamProfile2DBReader(**kwargs):
  mod = cms.EDAnalyzer('BeamProfile2DBReader',
    rawFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
