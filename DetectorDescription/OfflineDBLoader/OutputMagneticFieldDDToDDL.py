import FWCore.ParameterSet.Config as cms

def OutputMagneticFieldDDToDDL(**kwargs):
  mod = cms.EDAnalyzer('OutputMagneticFieldDDToDDL',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
