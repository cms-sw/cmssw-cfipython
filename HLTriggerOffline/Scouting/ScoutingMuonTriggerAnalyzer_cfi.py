import FWCore.ParameterSet.Config as cms

from .ScoutingMuonTriggerAnalyzer import ScoutingMuonTriggerAnalyzer

ScoutingMuonTriggerAnalyzer = ScoutingMuonTriggerAnalyzer(
  OutputInternalPath = 'MY_FOLDER',
  AlgInputTag = ('gtStage2Digis'),
  l1tAlgBlkInputTag = ('gtStage2Digis'),
  l1tExtBlkInputTag = ('gtStage2Digis')
)
