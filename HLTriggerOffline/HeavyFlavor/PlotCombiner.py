import FWCore.ParameterSet.Config as cms

def PlotCombiner(**kwargs):
  mod = cms.EDProducer('PlotCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
