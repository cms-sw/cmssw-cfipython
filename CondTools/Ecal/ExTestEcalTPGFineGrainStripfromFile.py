import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainStripfromFile(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainStripfromFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
