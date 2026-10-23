import FWCore.ParameterSet.Config as cms

def OutputMagneticFieldDDToDDL(*args, **kwargs):
  mod = cms.EDAnalyzer('OutputMagneticFieldDDToDDL',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
