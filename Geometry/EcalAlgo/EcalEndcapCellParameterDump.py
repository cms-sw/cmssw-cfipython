import FWCore.ParameterSet.Config as cms

def EcalEndcapCellParameterDump(**kwargs):
  mod = cms.EDAnalyzer('EcalEndcapCellParameterDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
