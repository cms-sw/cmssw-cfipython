import FWCore.ParameterSet.Config as cms

def TrackEfficiencyClient(**kwargs):
  mod = cms.EDProducer('TrackEfficiencyClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
