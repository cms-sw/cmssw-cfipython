import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGSpikeThresholdfromFile(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGSpikeThresholdfromFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
