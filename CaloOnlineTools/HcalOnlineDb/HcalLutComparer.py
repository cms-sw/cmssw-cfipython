import FWCore.ParameterSet.Config as cms

def HcalLutComparer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalLutComparer',
    lutXML1 = cms.string(''),
    lutXML2 = cms.string(''),
    verbosity = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
