import FWCore.ParameterSet.Config as cms

from .PFMETProducer import PFMETProducer

pfMetPuppi = PFMETProducer(
  src = ('particleFlow'),
  globalThreshold = 0,
  alias = '@module_label',
  calculateSignificance = False,
  parameters = cms.PSet(),
  applyWeight = True,
  srcWeights = ('puppiNoLep')
)
