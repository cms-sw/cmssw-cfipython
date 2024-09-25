import FWCore.ParameterSet.Config as cms

def ExTestEcalPulseSymmCovariancesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalPulseSymmCovariancesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
